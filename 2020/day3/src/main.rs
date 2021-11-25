// https://adventofcode.com/2020/day/3
use std::fs::File;
use std::io::*;

fn main() {
    let fname = "day3_input.txt";
    // part 1
    println!("{}", check_slope(fname, 3, 1));
    // part 2
    let result = check_slope(fname, 1, 1)
        * check_slope(fname, 3, 1)
        * check_slope(fname, 5, 1)
        * check_slope(fname, 7, 1)
        * check_slope(fname, 1, 2);
    println!("{}", result);
}

fn check_slope(fname: &str, right: usize, down: usize) -> usize {
    let file = File::open(fname).unwrap();
    let reader = BufReader::new(file);
    let mut lines = reader.lines().map(|l| l.unwrap());
    // advance iterator by 1 to skip first line
    lines.next();
    let mut x = right; // cursor to keep track of horizontal (x) position
    let mut y = 1; // cursor to keep track of vertical (y) position
    let mut trees = 0;
    for line in lines {
        if y % down != 0 {
            y += 1;
            continue;
        }
        let chars = line.chars().collect::<Vec<char>>();
        let adjusted_x = x % line.len();
        if chars.get(adjusted_x).unwrap() == &'#' {
            trees += 1;
        }
        x += right;
        y += 1;
    }
    trees
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn test_check_slope() {
        let fname = "test_input.txt";
        assert_eq!(check_slope(fname, 1, 1), 2);
        assert_eq!(check_slope(fname, 3, 1), 7);
        assert_eq!(check_slope(fname, 5, 1), 3);
        assert_eq!(check_slope(fname, 7, 1), 4);
        assert_eq!(check_slope(fname, 1, 2), 2);
    }
}
