
fn check_password(low : i32, high:i32, password:&str, value:&str) -> bool {
    let mut val = value.chars().next().unwrap();
    let val:Vec<_> = password.chars().filter(|i| *i==val).collect();

    if val.len() < (low as usize) || (high as usize )< val.len(){
        return false;
    }
    return true;
}

fn main() {
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
    println!("{}", count);
    }
