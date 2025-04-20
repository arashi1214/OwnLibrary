import React from 'react'

function BookForm() {
    return (
        <div>
            <form>
                <input type='txet' name='book_name' placeholder='請輸入書名'></input>
                <button type='submit'>搜尋</button>
            </form>
        </div>
    )
}

export default BookForm