use std::mem;

struct LinkedList {
    value:i32,
    next:Option<Box<LinkedList>>
}

impl LinkedList {
    pub fn add(&mut self, new_value:i32){

        match &mut self.next {
            Some(l) => {
                 l.add(new_value)
            },
            None=> self.next = Some(Box::new(LinkedList{value:new_value, next:None})),
        }

    }
    pub fn print_list(&self) {
        match &self.next {
            Some(l) => {
                println!("{}",self.value);
                 l.print_list()
            },
            None=>println!("{}",self.value),
        }
        }

    pub fn bubble_sort(&mut self) => LinkedList{
        let mut swaps = 0
        let mut head = self

        let mut prev = self
        let mut current = self.next
        //self is now empty
         loop{
            if let Some(l) = &mut current.next {
                println!("{}",self.value);

            }

        }

}

fn main() {

    let mut f = LinkedList {value:4, next: Some(Box::new(LinkedList {value:10, next:None})) };

    for x in 0..10 {
        f.add(x);
    }

    f.print_list();
}
