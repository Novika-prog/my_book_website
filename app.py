from flask import Flask, render_template

app = Flask(__name__)

books = [
    {
        'id': 1,
        'title': 'Buku Satu',
        'author': 'Pengarang Satu',
        'description': 'Deskripsi singkat tentang Buku Satu.'
    },
    {
        'id': 2,
        'title': 'Buku Dua',
        'author': 'Pengarang Dua',
        'description': 'Deskripsi singkat tentang Buku Dua.'
    },
    {
        'id': 3,
        'title': 'Buku Tiga',
        'author': 'Pengarang Tiga',
        'description': 'Deskripsi singkat tentang Buku Tiga.'
    }
]

@app.route('/')
def home():
    return render_template('index.html', books=books)

@app.route('/book/<int:book_id>')
def book_detail(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    return render_template('book_detail.html', book=book)

if __name__ == '__main__':
    app.run(debug=True)
