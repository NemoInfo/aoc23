use std::collections::HashMap;

use nom::{
    bytes::complete::tag,
    character::{complete::u32, streaming::newline},
    multi::{many1, separated_list1},
    sequence::tuple,
    IResult,
};

fn parse_list(input: &str) -> IResult<&str, Vec<u32>> {
    let (input, list) = separated_list1(many1(tag(" ")), u32)(input)?;

    Ok((input, list))
}

fn parse_card(input: &str) -> IResult<&str, (Vec<u32>, Vec<u32>)> {
    let (input, (_, winners, _, actual)) = tuple((
        tuple((tag("Card"), many1(tag(" ")), u32, tag(":"), many1(tag(" ")))),
        parse_list,
        tuple((tag(" |"), many1(tag(" ")))),
        parse_list,
    ))(input)?;

    Ok((input, (winners, actual)))
}

fn parse_file(input: &str) -> IResult<&str, Vec<(Vec<u32>, Vec<u32>)>> {
    let (input, cards) = separated_list1(newline, parse_card)(input)?;

    Ok((input, cards))
}

pub fn solve(input: &str) -> u32 {
    let (_input, cards) = parse_file(input).unwrap();

    let mut inventory: HashMap<u32, u32> = HashMap::new();

    for (i, (winners, actual)) in cards.iter().enumerate() {
        inventory.entry(i as u32).or_insert(1);

        let points = winners
            .iter()
            .filter(|winner| actual.iter().find(|x| x == winner).is_some())
            .count() as u32;

        for p in 1..points + 1 {
            *inventory.entry(i as u32 + p).or_insert(1) += 0 + inventory[&(i as u32)];
        }
    }

    inventory.values().sum()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_solve() {
        let input = std::fs::read_to_string("inputs/test.txt")
            .expect("ERROR: inputs/test.txt file not found");

        assert_eq!(solve(&input), 30);
    }
}
