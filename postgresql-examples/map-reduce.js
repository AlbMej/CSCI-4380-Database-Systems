db.zips.mapReduce(
    function() {
        emit(this._id, this.pop)
    },
    function(key, values) {
        return Array.sum(values)
    },
    {
        query: {},
        out: "zip_pop"
    }
)

// Create index of population by state
db.zips.mapReduce(
    function() {
        emit(this.state, this.pop)
    },
    function(key, values) {
        return Array.sum(values)
    },
    {
        query: {},
        out: "state_pop"
    }
)