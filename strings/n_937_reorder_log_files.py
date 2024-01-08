from utils.time_measurement import time_measurement


class ReorderLogs:
    @staticmethod
    @time_measurement
    def execute(logs: list[str]) -> list[str]:
        letter_logs = []
        digit_logs = []

        for log in logs:
            if log.split()[1].isdigit():
                digit_logs.append(log)
                continue
            letter_logs.append(log)

        letter_logs.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return letter_logs + digit_logs
