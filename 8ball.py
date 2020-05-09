#!/usr/bin/env python3
# -*- coding: iso-8859-1 -*-


import random


"""
Magic 8-ball - A program to answer all your questions
Copyright (C) 2020 Compass 
Website: https://8kun.top/slackware/
IRC Channels:
    #slackware@irc.rizon.net
    ##python@irc.rizon.net
    ##linux@irc.rizon.net

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
MA 02110-1301, USA.
"""


class Ball:
    """Class that represents an 8-ball program."""

    def __init__(self):
        """Initialize the attributes below if present."""

    def instructions(self):
        """Instructions of the 8-ball program."""
        # Print an introduction of the program.
        message = (
                "\nWelcome to the magic 8-ball!"
                "\nAsk me any question, and I will truthfully answer "
                "your woes!"
                )
        print(message)


    def question(self):
        """Ask the user a question."""
        """
        Ask the user his/her question. 'q' will quit the program, else
        it will continuously ask.
        """
        message = "\nAsk 8-ball a question ('q' to quit): "
        """
        If the user types 'q' the program will quit and print the
        message below, otherwise the user expects an answer and the
        method reply(self) is called.
        """
        while True:
            self.ask = input(message)
            if self.ask == 'q':
                print("Quitting 8-ball...")
                exit()
            else:
                # Call reply(self).
                print(self.reply())


    def reply(self):
        """Answer the user's question."""
        """
        All the answers could be in one single list, but dealing with
        three separate lists and combining them in one was
        more educational.
        """
        affirmative_answers = [
            'It is certain.', 'It is decidedly so.', 'Without a doubt.',
            'Yes - definitely.', 'You may rely on it.',
            'As I see it, yes.', 'Most likely.', 'Outlook good.',
            'Yes.', 'Signs point to yes.'
            ]
        non_committal_answers = [
            'Reply hazy, try again.', 'Ask again later.',
            'Better not tell you now.', 'Cannot predict now.',
            'Concentrate and ask again.'
            ]
        negative_answers = [
            'Don\'t count on it.', 'My reply is no.',
            'My sources say no.', 'Outlook not so good.', 'Very doubtful.'
            ]
        answers = (
            affirmative_answers + non_committal_answers
            + negative_answers
            )
        self.answer = random.choice(answers)
        return self.answer


test = Ball()
test.instructions()
test.question()
