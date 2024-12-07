package days

class Day6 : Day(6) {

    fun countDotsBeforeHashtag(input: String): Int {
        val hashtagIndex = input.indexOfFirst { it == '#' }
        return if (hashtagIndex == - 1) 0
        else input.substring(0, hashtagIndex).count { it == '.' }
    }

    fun noHashtag(input: String): Boolean = input.indexOfFirst { it == '#' } == -1

    fun findGuard(input: List<String>): Pair<Int, Int> {
        var found = false
        var index: Pair<Int, Int> = Pair(-1, -1)
        while (!found) {
            for ((i, s) in input.withIndex()) {
                for ((j, c) in s.withIndex()) {
                    index = Pair(i, j)
                    if (c == '^') found = true }
            }
            found = true
        }
        return index
    }


    override fun partOne(): Any {
        var orientation = 90 // 90 degrees corresponds to upwards hat ^
        var lastElem = ""
        var xCount = 0
        val rows = inputList
        var cols = rows[0].indices.map { colIndex ->
            rows.map { row -> row[colIndex] }
        }
        val start = findGuard(rows)
        val visited = mutableListOf<Pair<Int, Int>>()

        while (lastElem != ".") {

            when (orientation) {
                90  -> {

                    lastElem = if (noHashtag(rows[start.first])) rows.last() else "#"

                }
                180 -> {

                    lastElem = rows.last()

                }
                270 -> {}
                0   -> {}
            }

            orientation = (-90 + orientation) % 360
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