#!/usr/bin/env python3
"""
@desc    description
@author  ANGO <ango@afnor.org>
@version 0.0.1
@date    2020-12-01
@note    0.0.1 (2020-12-01) : Init file
"""

from typing import List
import pytest
from parsing.sentence_parser import SentenceParser


class TestSentenceParser:
    """SentenceParser test class.
    """

    @pytest.mark.parametrize(
        "sentence, expected_result",
        [
            (
                "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?",
                [
                    "Salut",
                    "GrandPy",
                    "Est",
                    "ce",
                    "que",
                    "tu",
                    "connais",
                    "l",
                    "adresse",
                    "d",
                    "OpenClassrooms",
                ],
            )
        ],
    )
    def test_split_words(self, sentence: str, expected_result: List[str]) -> None:
        """The split_words test method.
        Check if the method returns a right List of words from a sentence.
        """

        parser: SentenceParser = SentenceParser()
        parsed_sentence = parser.split_words(sentence)

        assert parsed_sentence == expected_result

    @pytest.mark.parametrize(
        "words_list, expected_result",
        [
            (
                [
                    "Salut",
                    "GrandPy",
                    "est",
                    "ce",
                    "que",
                    "tu",
                    "connais",
                    "l",
                    "adresse",
                    "d",
                    "OpenClassrooms",
                ],
                ["Salut", "GrandPy", "connais", "adresse", "OpenClassrooms",],
            )
        ],
    )
    def test_remove_stop_words(
        self, words_list: List[str], expected_result: List[str]
    ) -> None:
        """The remove_split_words test method.
        Check if the method returns a right List of words after removing stop words.
        """

        parser: SentenceParser = SentenceParser()
        clean_list = parser.remove_stop_words(words_list)

        assert clean_list == expected_result
