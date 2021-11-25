use std::fs::File;
use std::io::*;

fn main() {
    part_two();
}

fn part_one() -> Vec<i32> {
    let file = File::open("day5_input.txt").unwrap();
    let reader = BufReader::new(file);
    let lines = reader.lines().map(|l| l.unwrap());
    let mut max_seat_id = -1;
    let mut seat_ids = Vec::<i32>::new();
    for line in lines {
        let row = do_bisection(&line[0..7], 127, 'B');
        let col = do_bisection(&line[7..], 7, 'R');
        seat_ids.push(row * 8 + col);
        max_seat_id = std::cmp::max(max_seat_id, row * 8 + col);
    }
    println!("Max seat id: {}", max_seat_id);
    seat_ids
}

fn part_two() {
    let mut seat_ids = part_one();
    seat_ids.sort();
    let lower_check_bound = 1 * 8;
    let upper_check_bound = 126 * 8 + 7;

    for i in 0..seat_ids.len() {
        let id = seat_ids[i];
        if id > lower_check_bound && id < upper_check_bound - 2 {
            if seat_ids[i + 1] - id == 2 {
                println!("Your seat is {}", id + 1);
                return;
            }
        }
    }
}

fn do_bisection(code: &str, upper_bound: i32, upper_char: char) -> i32 {
    let mut lower = 0;
    let mut upper = upper_bound;
    for c in code.chars() {
        let mid = lower + (upper - lower) / 2;
        if c == upper_char {
            lower = mid + 1;
        } else {
            upper = mid;
        }
    }
    assert!(upper == lower);
    upper
}
