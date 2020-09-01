#!/usr/bin/env python3
import re
import sys
import os
import operator

def log_search(log_path):
        pattern = R"ticky: ([\w]*) ([\w ']*) (?:[\[\].# \d]* )?\(([\w.]*)"
        #1-type, 2-message, 3-user
        per_user_dict = {}
        error_dict = {}
        with open(log_path, mode="r", encoding="UTF-8") as f:
                for line in f.readlines():
                        result = re.search(pattern, line)
                        if result == None:
                            continue
                        else:
                            type, message, user = result.group(1,2,3)
                        #print(type(result), type(result[1]), result[2], result[3])
                        per_user_dict[user] = per_user_dict.get(user, {"INFO":0, "ERROR":0})
                        per_user_dict[user][type] = per_user_dict[user][type] + 1
                        if type == "ERROR":
                            error_dict[message] = error_dict.get(message, 0) + 1
        per_user_dict = sorted(per_user_dict.items())
        error_dict = sorted(error_dict.items(), key=operator.itemgetter(1), reverse=True)
        return per_user_dict, error_dict

def process_data(error_dict):
    pass

def dictionary_to_csv(dict_headers, data_dict, csv_path):
    pass


if __name__ == "__main__":
    log_path = "syslog.log"
    per_user_dict, error_dict = log_search(log_path)

    dict_headers = ["Username", "INFO", "ERROR"]
    csv_path = "user_statistics.csv"
    with open(csv_path, "w") as csvf:
        csvf.write(",".join(dict_headers)+"\n")
        for user, counters in per_user_dict:
            csvf.write(",".join([user, str(counters["INFO"]), str(counters["INFO"])])+"\n")

    dict_headers = ["Error", "Count"]
    csv_path = "error_message.csv"
    with open(csv_path, "w") as csvf:
        csvf.write(",".join(dict_headers)+"\n")
        for error, counter in error_dict:
            csvf.write(",".join([error, str(counter)])+"\n")

    #per_user_dict.insert(0, ("Username", "INFO", "ERROR"))
    #error_dict.insert(0, ("Error", "Count"))

    #dictionary_to_csv(per_user_dict_headers, per_user_dict, per_user_csv_path)
    #dictionary_to_csv(error_dict_headers, error_dict, error_csv_path)
    #print(per_user_dict, error_dict)
