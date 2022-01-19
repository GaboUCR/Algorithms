fn part_one(){
    let result = include_str!("../input.txt").lines();
    let mut trees:i32 = 0;
    let mut move_down = true;
    let mut right_moves = 3;

    for s in result {

        if move_down {
            move_down = false;
            continue;
        }

        let mut line = String::from("");

        for n in 0..100000{
            line.push_str(s);
        }

        for (i, c) in line.chars().enumerate() {
            if (i == right_moves){

                right_moves = right_moves + 3;
                // move_down = true;
                if c == "#".chars().next().unwrap() {
                    trees = trees + 1;
                }
                break;
            }

        }

    }
    println!("part one:{}", trees)
}

fn part_two(right:i32, down:i32) -> i32{
    let result = include_str!("../input.txt").lines();
    let mut trees:i32 = 0;
    let mut move_down = true;
    let mut right_moves = right;
    let mut moves_down = 0;

    for (i, s) in result.enumerate() {

        if (moves_down == down){
            move_down = false;
            moves_down = 0;
        }
        // println!("{}", moves_down);
        if move_down {
            moves_down = moves_down + 1;
            continue;
        }

        move_down = true;
        let mut line = String::from("");

        for n in 0..10000{
            line.push_str(s);
        }

        for (i, c) in line.chars().enumerate() {
            if (i == right_moves as usize){

                right_moves = right_moves + right;

                if c == "#".chars().next().unwrap() {
                    trees = trees + 1;
                }
                break;
            }

        }
        moves_down = moves_down + 1;
    }
    return trees;
}

fn main() {
    // part_one();
    println!("part one: {}", part_two(3, 1));
    // CALLING THEM TOGETHER CAUSED AN OVERFLOW
    // println!("part two: {}", part_two(3,1)*part_two(1,1)*part_two(5,1)*part_two(7,1)*part_two(1,2))

}
