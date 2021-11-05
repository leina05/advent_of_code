use std::fs::File;
use std::io::prelude::*;
use std::io::BufReader;

fn main() {
    let file = File::open("day1_input.txt").unwrap();
    let reader = BufReader::new(file);
    let mut nums: Vec<i64> = reader
        .lines()
        .into_iter()
        .map(|l| l.unwrap().parse::<i64>().unwrap())
        .collect();
    find_three(nums);
}

fn find_two(mut nums: Vec<i64>) {
    // Find two numbers that sum to 2020 and return their product
    nums.sort();
    for i in 0..nums.len() {
        let mut lower = i + 1;
        let mut upper = nums.len() - 1;
        while upper >= lower {
            let mid = lower + (upper - lower) / 2;
            let sum = nums[i] + nums[mid];
            if sum == 2020 {
                println!("{}", nums[i] * nums[mid]);
                return;
            } else if sum < 2020 {
                lower = mid + 1;
            } else {
                upper = mid - 1;
            }
        }
    }
}

fn find_three(mut nums: Vec<i64>) {
    // Find three numbers that sum to 2020 and return their product
    nums.sort();
    for i in 0..nums.len() {
        let mut lower = i + 1;
        let mut upper = nums.len() - 1;
        let target = 2020 - nums[i];

        while lower < upper {
            let sum = nums[lower] + nums[upper];
            if sum == target {
                println!("{}", nums[i] * nums[lower] * nums[upper]);
                return;
            } else if sum < target {
                lower += 1;
            } else {
                upper -= 1;
            }
        }
    }
}
