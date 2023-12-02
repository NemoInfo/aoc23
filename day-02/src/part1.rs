use std::collections::HashMap;

use nom::{
    branch::alt,
    bytes::complete::tag,
    character::complete::{newline, u8},
    multi::separated_list1,
    sequence::tuple,
    IResult,
};
use Color::*;

#[derive(Debug, Clone, Copy, PartialEq, Eq, Hash)]
enum Color {
    Red,
    Green,
    Blue,
}

fn parse_color(input: &str) -> IResult<&str, Color> {
    let (input, color) = alt((tag("red"), tag("green"), tag("blue")))(input)?;

    match color {
        "red" => Ok((input, Red)),
        "green" => Ok((input, Green)),
        "blue" => Ok((input, Blue)),
        _ => unreachable!("The `nom::branch::alt` shouldn't match anything else"),
    }
}

fn parse_round(input: &str) -> IResult<&str, HashMap<Color, u8>> {
    let (input, v) =
        separated_list1(tag(","), tuple((tag(" "), u8, tag(" "), parse_color)))(input)?;

    let map = v
        .iter()
        .map(|&(_, count, _, color)| (color, count))
        .collect::<HashMap<Color, u8>>();

    Ok((input, map))
}

fn parse_game(input: &str) -> IResult<&str, Vec<HashMap<Color, u8>>> {
    let (input, _) = tuple((tag("Game "), u8, tag(":")))(input)?;
    let (input, game) = separated_list1(tag(";"), parse_round)(input)?;

    Ok((input, game))
}

fn parse_file(input: &str) -> IResult<&str, Vec<Vec<HashMap<Color, u8>>>> {
    let (input, games) = separated_list1(newline, parse_game)(input)?;

    Ok((input, games))
}

pub fn solve(input: &str) -> u32 {
    let (_input, games) = parse_file(input).unwrap();

    let max_cubes = HashMap::from([(Red, 12), (Green, 13), (Blue, 14)]);

    games
        .iter()
        .enumerate()
        .map(|(idx, game)| {
            game.iter().all(|round| {
                round.iter().fold(true, |acc, (color, ammount)| {
                    acc && (max_cubes.get(color).unwrap() >= ammount)
                })
            }) as u32
                * (idx + 1) as u32
        })
        .sum()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_solve() {
        let input = std::fs::read_to_string("inputs/test.txt")
            .expect("ERROR: inputs/test.txt file not found");

        assert_eq!(solve(&input), 8);
    }
}
