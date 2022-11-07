import React from 'react'

const ListItem = ({set}) => {
  return (
    <div>
      <h3>{set.series.name} {set.set_number} - {set.title}</h3>
    </div>
  )
}

export default ListItem
