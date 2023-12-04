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

    cards
        .iter()
        .map(|(winners, actual)| {
            match winners
                .iter()
                .filter(|winner| actual.iter().find(|x| x == winner).is_some())
                .count()
                .checked_sub(1)
            {
                Some(p) => 2_u32.pow(p as u32),
                None => 0,
            }
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

        assert_eq!(solve(&input), 13);
    }
}
