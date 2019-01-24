import json


class JSONHandler:

    @staticmethod
    def read_from_file(file_path):
        with open(file_path) as raw_data:
            return json.loads(raw_data.read())

    @staticmethod
    def compare_two_json_objects(first, second):
        """Method compares two JSON objects.

        Args:
            first: first object.
            second: second object.
        Returns:
             comparison result as bool.
        """
        first, second = json.dumps(first, sort_keys=True), json.dumps(second, sort_keys=True)
        return first == second
