from utils.time_measurement import time_measurement


class TextJustification:
    @staticmethod
    @time_measurement
    def solution(words: list[str], max_width: int) -> list[str]:
        def justify_text(
            start: int, end: int, is_equal: bool, required_padding: int = 0
        ) -> str:
            # 만약 마지막 인덱스라면, 무조건 왼쪽 정렬한 값을 내보낸다
            if end == len(words) - 1:
                text = " ".join(words[i] for i in range(start, end + 1))
                return text + " " * (max_width - len(text))

            # 만약 패딩을 하나만 주었을 때, 맥스 길이에 맞춰서 떨어지는 경우
            if is_equal:
                return " ".join(words[i] for i in range(start, end + 1))

            # 패딩이 불규칙하게 적용되는 경우
            share, remain = (
                required_padding // end - start,
                required_padding % end - start,
            )
            text = words[start]
            for i in range(start + 1, end + 1):
                text += " " * share + words[i]
                if i == end:
                    text += " " * remain

            return text

        answer: list[str] = []
        current_index, start_index = 0, 0

        while start_index < len(words):
            current_text = None
            while True:
                if current_text is not None:
                    break

                estimated_word_length = sum(
                    len(words[i]) for i in range(start_index, current_index + 1)
                )
                padding_count = current_index - start_index

                if padding_count + estimated_word_length > max_width:
                    current_text = justify_text(
                        start_index,
                        current_index - 1,
                        False,
                        required_padding=max_width - estimated_word_length - 1,
                    )
                    current_index -= 1
                elif padding_count + estimated_word_length == max_width:
                    current_text = justify_text(start_index, current_index, True)

            answer.append(current_text)
            start_index, current_index = current_index + 1, current_index + 1

        return answer
