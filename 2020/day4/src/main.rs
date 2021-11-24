use std::collections::{HashMap, HashSet};
// use std::fmt::{Error, Result};
use regex::Regex;
use std::fs::File;
use std::io::*;
use std::result::Result;

fn main() {
    // part_one();
    part_two();
}

fn part_one() {
    let file = File::open("day4_input.txt").unwrap();
    // let file = File::open("test_input.txt").unwrap();
    let reader = BufReader::new(file);
    let lines = reader.lines().map(|l| l.unwrap());
    let mut fields = HashSet::<String>::new();
    let mut valid_passports = 0;
    for line in lines {
        if line.len() == 0 {
            // check fields
            if check_field_set(&fields) {
                valid_passports += 1;
            }
            fields.clear();
            continue;
        }
        let new_fields = line
            .split(" ")
            .map(|word| word.split(":").next().unwrap().to_owned())
            .collect::<HashSet<String>>();
        fields.extend(new_fields.clone())
    }
    // check the last line
    if check_field_set(&fields) {
        valid_passports += 1;
    }
    println!("valid passport count: {}", valid_passports);
}

fn check_field_set(fields: &HashSet<String>) -> bool {
    let required_fields: HashSet<String> = vec!["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
        .into_iter()
        .map(|s| s.to_owned())
        .collect();
    // check fields
    fields
        .intersection(&required_fields)
        .into_iter()
        .collect::<HashSet<&String>>()
        .len()
        == required_fields.len()
}

fn check_range(val: &str, min: usize, max: usize) -> Result<(), String> {
    let i_val = val.parse::<usize>().map_err(|e| e.to_string())?;
    if i_val < min || i_val > max {
        return Err(format!("Invalid field {}", val));
    }
    Ok(())
}

/// hgt (Height) - a number followed by either cm or in:
/// If cm, the number must be at least 150 and at most 193.
/// If in, the number must be at least 59 and at most 76.
fn check_hgt(hgt: &str) -> Result<(), String> {
    if hgt.ends_with("cm") {
        check_range(&hgt[0..hgt.len() - 2], 150, 193)
    } else if hgt.ends_with("in") {
        check_range(&hgt[0..hgt.len() - 2], 59, 76)
    } else {
        Err(format!("hgt missing units"))
    }
}
// hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
fn check_hcl(hcl: &str) -> Result<(), String> {
    let re = Regex::new(r"[0-9a-f]*").unwrap();
    if hcl.starts_with("#") && hcl.len() == 7 && re.is_match(&hcl[1..]) {
        Ok(())
    } else {
        Err(format!("bad hcl {}", hcl))
    }
}
// ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
fn check_ecl(ecl: &str) -> Result<(), String> {
    let valid_colors = vec!["amb", "blu", "brn", "gry", "grn", "hzl", "oth"];
    if valid_colors.contains(&ecl) {
        Ok(())
    } else {
        Err(format!("Invalid ecl {}", ecl))
    }
}
// pid (Passport ID) - a nine-digit number, including leading zeroes.
fn check_pid(pid: &str) -> Result<(), String> {
    let re = Regex::new(r"[0-9]*").unwrap();
    if pid.len() == 9 && re.is_match(pid) {
        Ok(())
    } else {
        Err(format!("Invalid pid {}", pid))
    }
}

fn check_valid_field(name: &str, val: &str) -> Option<String> {
    if match name {
        "byr" => check_range(val, 1920, 2002),
        "iyr" => check_range(val, 2010, 2020),
        "eyr" => check_range(val, 2020, 2030),
        "hgt" => check_hgt(val),
        "hcl" => check_hcl(val),
        "ecl" => check_ecl(val),
        "pid" => check_pid(val),
        _ => Err(format!("Bad field")),
    }
    .is_ok()
    {
        Some(name.to_owned())
    } else {
        None
    }
}

fn part_two() {
    let file = File::open("day4_input.txt").unwrap();
    // let file = File::open("test_input.txt").unwrap();
    let reader = BufReader::new(file);
    let lines = reader.lines().map(|l| l.unwrap());
    let mut fields = HashSet::<String>::new();
    let mut valid_passports = 0;
    for line in lines {
        if line.len() == 0 {
            // check fields
            if check_field_set(&fields) {
                valid_passports += 1;
            }
            fields.clear();
            continue;
        }
        // let mut new_fields = HashSet::new();
        let new_fields = line
            .split(" ")
            .filter_map(|word| {
                let mut iter = word.split(":").into_iter();
                let name = iter.next().unwrap();
                let val = iter.next().unwrap();
                check_valid_field(name, val)
            })
            .collect::<HashSet<String>>();
        fields.extend(new_fields.clone())
    }
    // check the last line
    if check_field_set(&fields) {
        valid_passports += 1;
    }
    println!("valid passport count: {}", valid_passports);
}
