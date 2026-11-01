from fastapi import APIRouter , Request
from service.games_service import GamesService as S
from models.game_model import GamesSchema, GamesModel

router = APIRouter()

@router.get("/api/games")
def get_all_games():
    with S() as s:
        games = s.get_all_games()
        return games
    
@router.get("/api/games/rating")
def get_rated_games_above(min_rating: float, order: str = "asc"):
    with S() as s:
        games = s.get_rated_min_threshhold(min_rating, order)
        return games

@router.get("/api/games/{id}")
def get_one_game(id:int):
    with S() as s:
        game = s.get_one_game(id)
        return game

@router.put("/api/games/{id}")
def update_game(id: int ,game_schema: GamesSchema):
    with S() as s:
        game_schema.id = id
        game = GamesModel(**game_schema.model_dump())
        db_product = s.update_game(game)
        return db_product
        

@router.post("/api/games", status_code= 201)
def add_one_game(game_schema: GamesSchema):
    with S() as s:
        game = GamesModel(**game_schema.model_dump())
        db_game = s.add_game(game)
        return db_game

@router.delete("/api/games/{id}", status_code= 204)
def delete_game(id:int):
    with S() as s:
        s.delete_game(id)

@router.get("/api/custom-one")
def get_custom1():
    with S() as s:
        studios_stats = s.custom_query1()
        return studios_stats

@router.get("/api/custom-two")
def get_custom2(genre: str):
    with S() as s:
        titles = s.custom_query(genre)
        return titles
 


    