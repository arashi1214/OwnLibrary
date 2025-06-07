import React from 'react'

function BookList() {
  return (
    <div>
        <h2>Book List</h2>
        <input type="text" placeholder="🔍 Search" class="search-input" />
        <div class="book-item">

            <div class="book-info">
                <h3>The Great Gatsby</h3>
                <p>F. Scott Fitzgerald</p>
                <p>Charles Scribner’s Sons</p>
            </div>
        </div>
    </div>
  )
}

export default BookList