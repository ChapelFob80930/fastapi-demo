from .. import schemas,models, utils, oauth2
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from sqlalchemy import func
from ..database import get_db
from typing import List, Optional



router = APIRouter( prefix = "/posts", tags = ['Posts'] ) 
#prefix for all routes in this router will be /posts
# tags = ['posts'] adds a tag to the routes in this router, which can be used for documentation purposes



# my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1},
#             {"title": "title of post 2", "content": "content of post 2", "id": 2}]

# def find_post(id):
#     for post in my_posts:
#         if post["id"] == id:
#             return post
        
# def find_index_post(id):
#     for i, post in enumerate(my_posts):
#         if post["id"] == id:
#             return i
        



# while True:   
    
#     try:
#         conn = psycopg2.connect(host = 'localhost',database = 'fastapi' ,user = 'postgres' ,password = 'Jitpdx@742004', cursor_factory = RealDictCursor)
#         cursor = conn.cursor()
#         print("Database connection was successful")
#         break
    
#     except Exception as error:
#         print("Connecting to Database Failed")
#         print("Error:", error)
#         time.sleep(2)

@router.get("/", response_model = List[schemas.PostOut]) #response_model is used to specify the response model for the route
async def get_posts(db: Session = Depends(get_db), current_user = Depends(oauth2.get_current_user), limit:int = 10, skip:int = 0, search: Optional[str] = ""):
    # cursor.execute("""SELECT * FROM posts""")
    # posts = cursor.fetchall()
    print(limit)
    # posts = db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all() #get all posts from the database, limit is used to limit the number of posts returned
    
    posts = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(models.Vote, models.Vote.post_id == models.Post.id, isouter = True).group_by(models.Post.id).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
    # This query joins the Post and Vote tables, counts the number of votes for each post, and groups the results by post id.
    # The func.count(models.Vote.post_id).label("votes") counts the number of votes for each post and labels it as "votes".
    
    return posts

@router.post("/", status_code=status.HTTP_201_CREATED, response_model = schemas.Post)
async def create_posts(post: schemas.PostCreate, db:Session = Depends(get_db), current_user = Depends(oauth2.get_current_user)):
    # # post_dict = post.dict()
    # # post_dict['id'] = randrange(0,1000000)
    # # my_posts.append(post_dict)
    
    # cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING *""", (post.title, post.content, post.published))
    # new_post = cursor.fetchone()
    
    # conn.commit()
    print(current_user.email)
    # new_post = models.Post(title = post.title, content = post.content, published = post.published) #inefficient if we have a lot of posts, but works for now
    
    new_post = models.Post(owner_id = current_user.id, **post.dict())#unpacking the post dictionary to match the Post model
    db.add(new_post)
    db.commit()
    db.refresh(new_post) #returns the newly created post with its id
    
    return new_post


@router.get("/{id}", response_model = schemas.PostOut)
def get_post(id: int, db: Session = Depends(get_db), current_user = Depends(oauth2.get_current_user)):
    # cursor.execute("""SELECT * FROM posts WHERE id = %s""", (str(id))) 
    # found_post = cursor.fetchone()
    
    # found_post = db.query(models.Post).filter(models.Post.id == id).first() #not use .all() as it searches for more posts even though we know the id is unique 
    
    found_post = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(models.Vote, models.Vote.post_id == models.Post.id, isouter = True).group_by(models.Post.id).filter(models.Post.id == id).first()
    
    if not found_post:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} was not found")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"message": f"Post with id {id} was not found"}
        #include response: Response in the function parameters to return a response with a status code
    
    return found_post

@router.delete("/{id}", status_code = status.HTTP_204_NO_CONTENT)
def delete_posts(id: int, db: Session = Depends(get_db), current_user = Depends(oauth2.get_current_user)):
    # # index = find_index_post(id)
    # cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING *""", (str(id),))
    # deleted_post = cursor.fetchone()
    # conn.commit()
    
    post_query = db.query(models.Post).filter(models.Post.id == id)
    
    post = post_query.first() 
    
    if post == None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Post with id {id} does not exist")
    # my_posts.pop(index)
    
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to perform requested action")
    
    post_query.delete(synchronize_session=False)
    db.commit()
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)    
    

@router.put("/{id}", response_model = schemas.Post) 
def update_posts(id: int, post: schemas.PostCreate, db: Session = Depends(get_db), current_user = Depends(oauth2.get_current_user)):
    # # index = find_index_post(id)
    
    # cursor.execute("""UPDATE posts SET title = %s, content=%s, published = %s WHERE id = %s RETURNING *""", (post.title, post.content, post.published, str(id)))
    
    # updated_post = cursor.fetchone()
    # conn.commit()
    
    post_query = db.query(models.Post).filter(models.Post.id == id)
    
    post_retrieved = post_query.first() 
    
    if post_retrieved == None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Post with id {id} does not exist")

    if post_retrieved.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to perform requested action")
    

    # post_dict = post.dict()
    # post_dict["id"] = id
    # my_posts[index] = post_dict
    
    post_query.update(post.dict(), synchronize_session = False) #input is a dictionary, so we can pass the post.dict() directly
    db.commit()
    
    return post_query.first() #return the updated post
