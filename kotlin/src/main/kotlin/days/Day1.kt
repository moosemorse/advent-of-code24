package days

class Day1 : Day(1) {

    override fun partOne(): Any {
        return inputList.take(2)
            .map { it.uppercase() }
            .joinToString(" ")
    }

    override fun partTwo(): Any {
        return inputString.split("\n")
            .filterNot { it.isEmpty() }
            .map { it.uppercase() }
            .last()
    }
}

fun main(args: Array<String>) {
    println(Day1().partOne())
    println(Day1().partTwo())
}
