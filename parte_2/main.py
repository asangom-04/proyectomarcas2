from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Ruta para la vista de lista
@app.route('/')
def movie_list():
    # Realizar consulta a la API para obtener una lista de películas
    api_key = "6214f274c799ca74fd8a2e0fed65e704"
    url = "https://api.themoviedb.org/3/movie/popular"
    params = {"api_key": api_key}
    response = requests.get(url, params=params)
    data = response.json()

    movies = data["results"]

    return render_template('movie_list.html', movies=movies)


# Ruta para la vista de detalle
@app.route('/movie/<movie_id>')
def movie_detail(movie_id):
    # Realizar consulta a la API para obtener los detalles de una película específica
    api_key = "6214f274c799ca74fd8a2e0fed65e704"
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    params = {"api_key": api_key}
    response = requests.get(url, params=params)
    movie = response.json()

    return render_template('movie_detail.html', movie=movie)


# Ruta para la vista de actores y personajes
@app.route('/movie/<movie_id>/cast')
def cast(movie_id):
    # Realizar consulta a la API para obtener los actores y personajes de una película
    api_key = "6214f274c799ca74fd8a2e0fed65e704"
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    params = {"api_key": api_key}
    response = requests.get(url, params=params)
    cast_data = response.json()

    cast = cast_data["cast"]

    return render_template('cast.html', cast=cast)


# Ruta para el formulario de filtrado
@app.route('/search', methods=['GET', 'POST'])
def movie_search():
    if request.method == 'POST':
        # Obtener el término de búsqueda ingresado por el usuario
        search_query = request.form['search_query']

        # Realizar consulta a la API para buscar películas basadas en el término de búsqueda
        api_key = "6214f274c799ca74fd8a2e0fed65e704"
        url = "https://api.themoviedb.org/3/search/movie"
        params = {
            "api_key": api_key,
            "query": search_query
        }
        response = requests.get(url, params=params)
        data = response.json()

        movies = data["results"]

        return render_template('movie_list.html', movies=movies)

    return render_template('search_form.html')


if __name__ == '__main__':
    app.run()
