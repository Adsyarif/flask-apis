from flask import Blueprint, jsonify


pokemon_blp = Blueprint("pokemon_pendpoint", __name__)

pokemon = [
    {
        "name": "Coco",
        "atribute": "Fire",

    },
    {
        "name": "Caca",
        "atribute": "Ice",

    }
]


@pokemon_blp.route("/", methods=["GET"])
def get_pokemon():
    return jsonify(pokemon)


@pokemon_blp.route("/", methods=["POST"])
def create_pokemon():
    return "GET ALL POKEMON"


@pokemon_blp.route("/pokemon/<string:pokemon_id>", methods=["PUT"])
def update_pokemon(pokemon_id):
    return (pokemon_id)


@pokemon_blp.route("/<string:pokemon_id>", methods=["DELETE"])
def delete_pokemon():
    return "GET ALL POKEMON"
