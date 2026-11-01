from utils.dal import Dal
from models.game_model import GamesModel as M
from sqlalchemy import desc, asc , text
from fastapi import HTTPException, status
from typing import cast
from models.game_model import GamesModel
import math

class GamesService:

    def __init__(self) -> None:
        self.session = Dal.create_session()

    def get_all_games(self):
        games = self.session.query(M).all()
        return games

    def get_one_game(self,id: int):
        game = self.session.get(M, id)
        if not game:
            raise HTTPException(status_code= 404, detail= f"Game {id} not found...")
        return game 

    def add_game(self, game: GamesModel):

        self.session.add(game)
        self.session.commit() # Commits the add of game
        self.session.refresh(game) # Refereshes the session to fetch the same product after refreshed
        return game

    def update_game(self, game: GamesModel):

        id = cast(int,game.id) # Casts Int upon game.id
        self.get_one_game(id) # Prevent 404 updating an the air basically

        db_game = self.session.merge(game) # Its like git hub first add / merge then commit which is like push basically for the db
        self.session.commit()
        self.session.refresh(db_game)

    def delete_game(self, id: int):

        game = self.get_one_game(id) # Prevents 404
        self.session.delete(game)
        self.session.commit() # Push to db no need to refresh cause there is no echo

    def get_rated_min_threshhold(self, min_rating: float, order: str):

        shapeshifter = desc if order.lower() == "desc" else asc

        if not (10 >= min_rating >= 0):
            raise HTTPException(status_code=422, detail= "Rating in the params must be between 10 and 0")

        games = self.session.query(M).where(M.rating > min_rating).order_by(shapeshifter(M.rating)).all()
        return games
            
    def custom_query1(self):

        sql = text("""
        select studios.name as studio , count(games.id) as game_count, round(avg(price),2) as avg_price
        from games
        right join studios on games.studio_id = studios.id
        group by studios.id, studios.name
        order by studio
        """)

        studios_stats = self.session.execute(sql).mappings().all()


        return studios_stats

    def custom_query(self, genre: str):

        genres = self.get_genres()
        is_valid_genre = any(genre.lower() == g.lower() for g in genres)
        if not is_valid_genre:
            raise HTTPException(status_code=422, detail= f"Gerne {genre} not valid this are the valid gernes {genres}")

        sql = text("""
            select games.title, studios.name as studio, games.price
            from games
            left join studios on games.studio_id = studios.id
            where games.genre = :genre
            order by games.title
            """)

        titles = self.session.execute(sql, {"genre": genre}).mappings().all()

        return titles

    def get_genres(self):

        sql = text("select distinct(genre) from games")
        genres = self.session.execute(sql).scalars().all()
        return genres



    
        




   


    def close(self):
        self.session.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        self.close()