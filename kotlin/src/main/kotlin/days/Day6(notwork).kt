package days

class Day6 : Day(6) {

//    fun countDotsBeforeHashtag(input: String): Int {
//        val hashtagIndex = input.indexOfFirst { it == '#' }
//        return if (hashtagIndex == - 1) 0
//        else input.substring(0, hashtagIndex).count { it == '.' }
//    } I think there's a way I could use this but not sure

    fun noHashtag(input: String): Boolean = input.indexOfFirst { it == '#' } == -1

    fun findGuard(input: List<String>): Pair<Int, Int> {
            for ((i, s) in input.withIndex()) {
                for ((j, c) in s.withIndex()) {
                    if (c == '^') return Pair(i, j)
        }
    }
        return Pair(-1, -1) }

    fun processPath(xCount: MutableList<Int>, path: String, orientation: Int,
                    current: Pair<Int, Int>, visited: MutableList<Pair<Int, Int>>)
                    : Pair<Pair<Int, Int>, String> {
        for ((i, c) in path.withIndex()) {
            val currIndex = if (orientation == 90 || orientation == 180) path.length - i - 1 else i
            if ((c == '.' || c == '^') && Pair(currIndex, current.second) !in visited) {
                visited.add(currIndex to current.second)
                xCount[0]++
                return Pair(Pair(currIndex, current.second), ".")
            }
        }
        return Pair(current, "#")
    }

//    fun isValidMove(path: String, currIndex: Int, visited: MutableList<Pair<Int, Int>>, current: Pair<Int, Int>): Boolean {
//        return (path[currIndex] == '.' || path[currIndex] == '^') &&
//                (Pair(currIndex, current.second) !in visited)
//    }

    override fun partOne(): Any {
        var lastElem = ""
        var xCount = mutableListOf(0)
        val rows = inputList
        val cols = rows[0].indices.map { colIndex ->
            rows.map { row -> row[colIndex] }.joinToString("")
        }
        var current = findGuard(rows) // 1) Find starting point and combined with orientation, we can traverse path
        var orientation = 90 // 90 degrees corresponds to upwards hat ^
        val visited = mutableListOf<Pair<Int, Int>>()

        while (lastElem != ".") {
            // Steps of algo: if current char is '.' and the index of this point hasn't been visited yet
            // - Then we store the index (in the context of a 2D grid - list of lists of rows)
            // - Increment xCount
            // - Update current point (so move to next point in path)
            // - After iteration we find the last element in the path to check if we can break from while statement
            // else -> update orientation (rotate our hat character 90 degrees clockwise
            when (orientation) {
                90  -> {
                    val path = cols[current.second]
                    val result = processPath(xCount, path, 90, current, visited)
                    lastElem = if (noHashtag(path.substring(0, current.first))) "." else "#"
                }
                180 -> {
                    val path = rows[current.first]
                    val result = processPath(xCount, path, 180, current, visited)
                    lastElem = if (noHashtag(path.substring(0, current.second))) path.first().toString() else "#"
                }
                270 -> {
                    val path = cols[current.second]
                    val result = processPath(xCount, path, 270, current, visited)
                    lastElem = if (noHashtag(path.substring(current.first))) path.last().toString() else "#"
                }
                0   -> {
                    val path = rows[current.first]
                    val result = processPath(xCount, path, 0, current, visited)
                    lastElem = if (noHashtag(path.substring(current.second))) path.last().toString() else "#"
                }
            }

            orientation = (orientation - 90) % 360
        }

        return xCount
    }

    override fun partTwo(): Any {
        TODO("Not yet implemented")
    }
}

fun main(args: Array<String>) {
    println(Day6().partOne())
}