import React from 'react'
import PropTypes from 'prop-types'


import BookDetail from './BookDetail';
import BookList from './BookList';

function Bookpage(props) {
  return (
    <div className="App">
        <div className='container'>
            <BookList></BookList>
            <BookDetail></BookDetail>
        </div>
    </div>
  )
}

Bookpage.propTypes = {}

export default Bookpage


