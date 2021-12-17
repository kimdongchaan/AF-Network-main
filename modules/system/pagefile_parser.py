import sys
import yara

class StartYara():
    def __init__(self):
        self.rule_path = r"C:\AF-Network-main\modules\pagefile_yara_rule.yar"

    def get_yara_return(self, data):
        self.matched_result = data["strings"]

    def rule_compile(self, rule_file_path):
        rules = yara.compile(filepath=rule_file_path)
        return rules

    def rule_match_string(self, compiled_rules, target_file_name):
        try:
            t_file = open(target_file_name, "rb")
            self.file_data = t_file.read()
            compiled_rules.match(data=self.file_data, callback=self.get_yara_return)
            self.file_data = 0
        except Exception as e:
            print(e)
            return

        onion_list =[]
        for value in self.matched_result:
            onion_list.append(value[2].decode('utf-8')[7:])
            #onion_list = (value[2].decode('utf-8')[7:])

        return onion_list


    def yara_run(self, target):
        rules = self.rule_compile(self.rule_path)
        return self.rule_match_string(rules, target)

def execute(target_path):
    result = StartYara()
    return result.yara_run(target_path)

if __name__ == "__main__":
    execute(sys.argv[0])