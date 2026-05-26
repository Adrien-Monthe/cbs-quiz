#!/usr/bin/env python3
"""
CBS Core Knowledge Quiz - Python CLI version

Usage:
    python quiz.py

Picks 20 random questions from the 300-question pool, asks one by one,
shows the explanation, and gives you a final score.
Scores are saved locally to scores.json — a simple leaderboard.

No external dependencies (standard library only).
"""

import json
import os
import random
import sys
import time
from datetime import datetime
from pathlib import Path

# ---- Paths ---------------------------------------------------------------
HERE = Path(__file__).parent
QUESTIONS_FILE = HERE / "questions.json"
SCORES_FILE = HERE / "scores.json"
QUIZ_LENGTH = 20

# ---- ANSI colors (works on most modern terminals) ------------------------
class C:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    GREEN = "\033[92m"
    RED = "\033[91m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    MAGENTA = "\033[95m"

# Disable colors on Windows terminals that don't support ANSI
if os.name == "nt":
    try:
        import ctypes
        kernel32 = ctypes.windll.kernel32
        kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
    except Exception:
        # If we can't enable ANSI, strip the codes
        for attr in dir(C):
            if not attr.startswith("_"):
                setattr(C, attr, "")


def clear_screen() -> None:
    os.system("cls" if os.name == "nt" else "clear")


def load_questions() -> list:
    if not QUESTIONS_FILE.exists():
        print(f"{C.RED}Error: {QUESTIONS_FILE} not found.{C.RESET}")
        sys.exit(1)
    with QUESTIONS_FILE.open("r", encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, list) or len(data) < QUIZ_LENGTH:
        print(f"{C.RED}Error: questions.json is empty or too short.{C.RESET}")
        sys.exit(1)
    return data


def load_scores() -> list:
    if not SCORES_FILE.exists():
        return []
    try:
        with SCORES_FILE.open("r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []


def save_score(entry: dict) -> None:
    scores = load_scores()
    scores.append(entry)
    with SCORES_FILE.open("w", encoding="utf-8") as f:
        json.dump(scores, f, indent=2)


def banner() -> None:
    print(f"{C.CYAN}{C.BOLD}")
    print("=" * 60)
    print("        CBS CORE KNOWLEDGE QUIZ - 20 Random Questions")
    print("=" * 60)
    print(f"{C.RESET}")


def ask_question(q: dict, n: int, total: int) -> bool:
    """Return True if answer correct."""
    print(f"{C.DIM}[{q['topic']}]{C.RESET}")
    print(f"{C.BOLD}Question {n}/{total}:{C.RESET} {q['q']}\n")
    for i, opt in enumerate(q["options"]):
        letter = chr(ord("A") + i)
        print(f"  {C.CYAN}{letter}.{C.RESET} {opt}")
    print()

    while True:
        ans = input(f"{C.YELLOW}Your answer (A/B/C/D, or Q to quit): {C.RESET}").strip().upper()
        if ans == "Q":
            print(f"{C.YELLOW}Quitting…{C.RESET}")
            sys.exit(0)
        if ans in ("A", "B", "C", "D"):
            picked = ord(ans) - ord("A")
            break
        print(f"{C.RED}Please enter A, B, C, or D.{C.RESET}")

    correct = (picked == q["correct"])
    correct_letter = chr(ord("A") + q["correct"])

    if correct:
        print(f"\n{C.GREEN}{C.BOLD}✓ Correct!{C.RESET}")
    else:
        print(f"\n{C.RED}{C.BOLD}✗ Not quite.{C.RESET} The correct answer was {C.GREEN}{correct_letter}{C.RESET}.")
    print(f"{C.BLUE}{C.BOLD}Tip:{C.RESET} {q['tip']}\n")

    input(f"{C.DIM}Press Enter for the next question…{C.RESET}")
    return correct


def show_leaderboard() -> None:
    clear_screen()
    scores = load_scores()
    print(f"{C.CYAN}{C.BOLD}🏆  LEADERBOARD  🏆{C.RESET}\n")
    if not scores:
        print(f"{C.DIM}No scores recorded yet.{C.RESET}")
        return
    scores.sort(key=lambda s: (-s["score"], s.get("seconds", 9999)))
    print(f"{C.BOLD}{'#':<4} {'Name':<24} {'Score':<10} {'%':<6} {'When':<12}{C.RESET}")
    print("-" * 60)
    for i, s in enumerate(scores[:25], 1):
        when = s.get("date", "")[:10]
        score_str = f"{s['score']}/{s['total']}"
        print(f"{i:<4} {s['name'][:24]:<24} {score_str:<10} {s['pct']:<5}% {when}")


def run_quiz(all_q: list, player: str) -> None:
    picked = random.sample(all_q, QUIZ_LENGTH)
    score = 0
    wrong = []
    start = time.time()

    for i, q in enumerate(picked, 1):
        clear_screen()
        banner()
        print(f"{C.DIM}Player: {player}  |  Score so far: {score}/{i-1}{C.RESET}\n")
        if ask_question(q, i, QUIZ_LENGTH):
            score += 1
        else:
            wrong.append(q)

    elapsed = int(time.time() - start)
    pct = round(score / QUIZ_LENGTH * 100)

    clear_screen()
    banner()
    print(f"{C.BOLD}Results for {player}{C.RESET}\n")
    if pct >= 90:
        verdict = f"{C.GREEN}🏆 Outstanding!{C.RESET}"
    elif pct >= 75:
        verdict = f"{C.GREEN}🎉 Great job!{C.RESET}"
    elif pct >= 60:
        verdict = f"{C.YELLOW}👍 Good progress!{C.RESET}"
    elif pct >= 40:
        verdict = f"{C.YELLOW}📚 Getting there…{C.RESET}"
    else:
        verdict = f"{C.RED}😅 Keep practicing!{C.RESET}"
    print(verdict)
    print(f"\n{C.BOLD}Final Score: {C.CYAN}{score} / {QUIZ_LENGTH}{C.RESET}  ({pct}%)")
    print(f"Time taken: {elapsed} seconds\n")

    if wrong:
        print(f"{C.MAGENTA}{C.BOLD}Review — questions you missed:{C.RESET}")
        for q in wrong:
            correct_letter = chr(ord("A") + q["correct"])
            print(f"\n  {C.DIM}[{q['topic']}]{C.RESET} {q['q']}")
            print(f"  {C.GREEN}Correct: {correct_letter}. {q['options'][q['correct']]}{C.RESET}")
            print(f"  {C.DIM}{q['tip']}{C.RESET}")

    save_score({
        "name": player,
        "score": score,
        "total": QUIZ_LENGTH,
        "pct": pct,
        "seconds": elapsed,
        "date": datetime.now().isoformat(timespec="seconds"),
    })


def menu(all_q: list) -> None:
    while True:
        clear_screen()
        banner()
        print(f"  {C.CYAN}1.{C.RESET} Take the quiz (20 random questions)")
        print(f"  {C.CYAN}2.{C.RESET} View leaderboard")
        print(f"  {C.CYAN}3.{C.RESET} Quit\n")
        choice = input(f"{C.YELLOW}Your choice: {C.RESET}").strip()
        if choice == "1":
            player = input(f"{C.YELLOW}Enter your name: {C.RESET}").strip() or "Anonymous"
            run_quiz(all_q, player)
            input(f"\n{C.DIM}Press Enter to return to the menu…{C.RESET}")
        elif choice == "2":
            show_leaderboard()
            input(f"\n{C.DIM}Press Enter to return to the menu…{C.RESET}")
        elif choice == "3":
            print(f"{C.CYAN}Goodbye!{C.RESET}")
            return
        else:
            print(f"{C.RED}Please choose 1, 2, or 3.{C.RESET}")
            time.sleep(1)


if __name__ == "__main__":
    try:
        questions = load_questions()
        menu(questions)
    except KeyboardInterrupt:
        print(f"\n{C.YELLOW}Interrupted. Bye!{C.RESET}")
