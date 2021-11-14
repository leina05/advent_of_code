use std::collections::HashSet;
use std::fs::File;
use std::io::prelude::*;
use std::io::BufReader;

fn main() {
    part_one();
    part_two();
}

fn part_one() {
    let file = File::open("day2_input.txt").unwrap();
    let reader = BufReader::new(file);
    let count = reader
        .lines()
        .into_iter()
        .filter(|line| {
            let line = line.as_ref().unwrap();
            let words = line.split(" ").collect::<Vec<&str>>();
            let mut splitter = words[0].split("-");
            let lower = splitter.next().unwrap().parse::<usize>().unwrap();
            let upper = splitter.next().unwrap().parse::<usize>().unwrap();
            let letter = words[1].chars().next().unwrap();
            let password = words[2];
            let count = password.chars().filter(|l| l == &letter).count();
            count >= lower && count <= upper
        })
        .count();
    println!("{}", count);
}

fn part_two() {
    let file = File::open("day2_input.txt").unwrap();
    let reader = BufReader::new(file);
    let count = reader
        .lines()
        .into_iter()
        .filter(|line| {
            let line = line.as_ref().unwrap();
            let words = line.split(" ").collect::<Vec<&str>>();
            let mut splitter = words[0].split("-");
            let first = splitter.next().unwrap().parse::<usize>().unwrap();
            let second = splitter.next().unwrap().parse::<usize>().unwrap();
            let letter = words[1].chars().next().unwrap();
            let password = words[2];
            let mut set = HashSet::new();
            set.insert(password.chars().nth(first - 1).unwrap());
            set.insert(password.chars().nth(second - 1).unwrap());
            set.contains(&letter) && set.len() == 2
        })
        .count();
    println!("{}", count);
}
