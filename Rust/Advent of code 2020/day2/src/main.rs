
fn check_password(low : i32, high:i32, password:&str, value:&str) -> bool {
    let val = value.chars().next().unwrap();
    let val:Vec<_> = password.chars().filter(|i| *i==val).collect();

    if val.len() < (low as usize) || (high as usize )< val.len(){
        return false;
    }
    return true;
}

fn part_one(){
    let result = include_str!("../input.txt").lines().map(|i| i.split(":"));
    // create an iterator that we can use whenever we want
    //At this point the splitted strings are not computed yet.
    let mut count:i32 = 0;

    for s in result{ //Go over the iterator and compute the results when needed
        let st : Vec<_> = s.take(2).collect();

        let mut bounds = st[0].split("-");
        let low = bounds.next().unwrap().parse::<i32>().unwrap();

        let mut temp = bounds.next().unwrap().split(" ");
        let high = temp.next().unwrap().parse::<i32>().unwrap();

        let value = temp.next().unwrap();
        let password = st[1];

        if check_password(low, high, password, value) {
            count = count + 1;
        }
    }
    println!("part one: {}", count);
}

fn check_password_part_two(low:i32, high: i32, password: &str, value:&str) -> bool{
    let mut is_low = false;
    let mut is_high = false;
    let mut code = value.chars().next().unwrap();


    for (i, c) in password.chars().enumerate() {
        if (i == 0){
            continue
        }

        if (i == ((low) as usize) ) {
            if(c == code){
                is_low = true;
            }
        }

        if (i == ((high) as usize) ) {

            if (c == code) {
                is_high = true
            }
        }
    }

    if(is_low == true && is_high == false){
        return true
    }

    else if(is_high == true && is_low == false){
        return true
    }
    else {
        return false
    }
}

fn part_two(){
    let result = include_str!("../input.txt").lines().map(|i| i.split(":"));
    // create an iterator that we can use whenever we want
    //At this point the splitted strings are not computed yet.
    let mut count:i32 = 0;

    for s in result{ //Go over the iterator and compute the results when needed
        let st : Vec<_> = s.take(2).collect();

        let mut bounds = st[0].split("-");
        let low = bounds.next().unwrap().parse::<i32>().unwrap();

        let mut temp = bounds.next().unwrap().split(" ");
        let high = temp.next().unwrap().parse::<i32>().unwrap();

        let value = temp.next().unwrap();
        let password = st[1];

        if check_password_part_two(low, high, password, value) {
            count = count + 1;
        }
    }
    println!("part two: {}", count)
}

fn main() {
    part_one();
    part_two();
}
