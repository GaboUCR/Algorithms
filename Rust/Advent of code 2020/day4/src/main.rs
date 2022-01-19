fn part_one(){
    let data = include_str!("input.txt").lines();
    let mut count:i32 = 0;
    let mut valid_fields:i32 = 0;

    for s in data {
        if s.is_empty(){

            valid_fields = 0;
            continue;
        }

        let credentials = s.split(" ");

        for c in credentials {
            let fields = c.split(":");

            let st : Vec<_> = fields.take(2).collect();
            if (st[0]=="cid"){
                continue;
            }
            else{
                valid_fields += 1;
            }
        }
        if (valid_fields == 7){
            count += 1;
            valid_fields = 0;
        }
    }
    println!("part one: {}", count);
}

fn is_int_between (low:i32, high:i32, value:i32) -> bool{
    if value >= low && high >= value {
        return true;
    }
    false
}

fn part_two(){
    let data = include_str!("input.txt").lines();
    let mut count:i32 = 0;
    let mut valid_fields:i32 = 0;

    for s in data {

        if s.is_empty() {
            valid_fields = 0;
            continue;
        }

        let credentials = s.split(" ");

        for c in credentials {
            let fields = c.split(":");

            let st : Vec<_> = fields.take(2).collect();
            match st[0] {
                "cid" => continue,

                "byr" => {
                    if is_int_between(1920, 2002, st[1].parse::<i32>().unwrap()) {
                        valid_fields += 1;
                        continue;
                    }
                },
                "iyr" => {
                    if is_int_between(2010, 2020, st[1].parse::<i32>().unwrap()) {
                        valid_fields += 1;
                        continue;
                    }
                },
                "eyr" => {
                    if is_int_between(2020, 2030, st[1].parse::<i32>().unwrap()) {
                        valid_fields += 1;
                        continue;
                    }
                },
                "hgt" => {
                    if (st[1].ends_with("cm")) {
                        if is_int_between(150, 193, st[1][..st[1].len()-2].parse::<i32>().unwrap()){
                            valid_fields += 1;
                            continue;
                        }
                    }
                    else if(st[1].ends_with("in")){
                        if is_int_between(59, 76, st[1][..st[1].len()-2].parse::<i32>().unwrap()){
                            valid_fields += 1;
                            continue;
                        }
                    }
                },
                "hcl" => {
                    let valid_values = String::from("#0123456789abcdef");
                    let hastag = String::from("#");
                    let mut valid = true;

                    for (i, s) in st[1].chars().enumerate() {

                        if (i == 0 && s != hastag.chars().next().unwrap()) {
                            valid = false;
                            break;
                        }
                        if (st[1].len() != 7){

                            valid = false;
                            break;
                        }
                        if (valid_values.find(s) == None){

                            valid = false;
                            break;
                        }
                    }
                    if (valid){
                        valid_fields += 1;
                        continue;
                    }
                },
                "ecl" => {
                    if (st[1] == "amb" || st[1]=="blu" || st[1] =="brn"|| st[1]=="gry"||st[1]=="grn"|| st[1]=="hzl"||st[1]=="oth"){
                        valid_fields += 1;
                        continue;
                    }
                },
                "pid" => {
                    let valid_values = String::from("0123456789");
                    let mut valid = true;

                    for s in st[1].chars() {
                        match valid_values.find(s) {
                            Some(_x) => {
                                valid = true;
                            },
                            None => {
                                valid = false;
                                break;
                            },

                        }

                        if (st[1].len() != 9){
                            valid = false;
                            break
                        }
                    }

                    if (valid){
                        valid_fields += 1;
                        continue;
                    }

                },
                _ => {continue;},
            }
        }
        if (valid_fields == 7){
            count += 1;
            valid_fields = 0;
        }
        }
    println!("part two:{}", count);
    }



fn main() {
    part_one();
    part_two();
}
