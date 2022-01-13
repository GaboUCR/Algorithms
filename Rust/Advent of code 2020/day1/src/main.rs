use itertools::Itertools;

pub fn main() {
    // part 1
    let result : Vec<_> =
                include_str!("../input.txt")
                .lines()
                .map(|i| i.parse::<usize>().unwrap()) //cast string to arquitecture size int
                .combinations(2) // creates iter with every combination of 2 elements
                .filter(|i| i.iter().sum::<usize>() == 2020) //creates iter with elements that add up to 2020
                .collect(); // place them on a Vec

    println!("Part 1: {}\n", result[0][0]*result[0][1]); //filter returns a iter of iters, hence the double []
    //part 2
    let result : Vec<_> =
                include_str!("../input.txt")
                .lines()
                .map(|i| i.parse::<usize>().unwrap()) //cast string to arquitecture size int
                .combinations(3) // creates iter with every combination of 2 elements
                .filter(|i| i.iter().sum::<usize>() == 2020) //creates iter with elements that add up to 2020
                .collect(); // place them on a Vec

    println!("Part 2: {}\n", result[0][0]*result[0][1]*result[0][2]);
}
