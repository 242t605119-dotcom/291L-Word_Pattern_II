# LeetCode 291 - Word Pattern II

## Problem Statement

Given a pattern and a string `s`, determine if `s` follows the same pattern.

Each character in the pattern must map to a non-empty substring of `s`.

The mapping must be:

* Consistent
* One-to-one
* Each character maps to only one substring
* Two different characters cannot map to the same substring

## Example

### Input

```text
pattern = "abab"
s = "redblueredblue"
```

### Output

```text
true
```

### Explanation

The mapping is:

```text
a → red
b → blue
```

So:

```text
a b a b
red blue red blue
```

The pattern matches the string.

## Approach

We use **Backtracking**.

1. Start from the first character of the pattern.
2. If the character already has a mapping, check whether the mapped word matches the current part of the string.
3. If it does not have a mapping, try every possible substring.
4. Store the mapping temporarily.
5. Continue recursively.
6. If a choice fails, remove the mapping and try another substring.
7. Return `true` when the complete pattern and string are matched.

## Algorithm

```text
Start from pattern[0] and s[0]

If the pattern character already has a mapping:
    Check whether the mapped substring matches s
    If yes, continue
    Otherwise return false

If the character has no mapping:
    Try every possible substring
    Make the mapping
    Continue with backtracking
    If it fails, remove the mapping

If the complete pattern and string are matched:
    return true
```

## Time Complexity

`O(n^m)` in the worst case, where `m` is the length of the pattern and `n` is the length of the string.

## Space Complexity

`O(m + n)` for the recursion stack and mappings.

## Author

T. Nandhini
