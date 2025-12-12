#!/usr/bin/env sh

if [ -z "$1" ]; then
  echo "Usage: $0 <day_number>"
  exit 1
fi

DAY=$(printf "%02d" "$1")
DIR="day${DAY}"

if [ -d "$DIR" ]; then
  echo "Directory $DIR already exists."
  exit 1
fi

mkdir "$DIR" || exit 1

touch "$DIR/example.txt"
touch "$DIR/input.txt"
touch "$DIR/part1.py"
touch "$DIR/part2.py"

echo "Created structure for $DIR"