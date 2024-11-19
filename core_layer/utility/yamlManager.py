import yaml
import os
import multiprocessing

get_root_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

class YamlUtilities:

    __yaml_data = None

    def read_from_yaml_file(self, filename):
        """
        Read and parse a YAML file and store its contents.
        :return: The data parsed from the YAML file as a Python dictionary.
        """
        yaml_file_path = os.path.join(get_root_directory, 'config', filename + '.yml')

        lock = multiprocessing.Lock()
        lock.acquire()
        try:
            with open(yaml_file_path, 'r') as file:
                self.__yaml_data = yaml.safe_load(file)
        finally:
            lock.release()

        return self.__yaml_data

    def get_data_from_yaml(self, key):
        """
        Retrieve a specific value from the YAML data by its key.
        :param key: The key to look up in the YAML data.
        :return: The value associated with the specified key.
        :raises Exception: If the key is not found in the YAML data.
        """
        if key in self.__yaml_data:
            return self.__yaml_data[key]
        else:
            raise Exception(f'Key "{key}" is not found in the YAML file')

    def write_to_yaml_file(self, yaml_data, filename):
        """
            Write data to a YAML file.
            :param yaml_data: The data to be written to the YAML file
            :param name_of_yaml_file: The base name of the YAML file (without the .yml extension) where data will be written.
            """
        yaml_file_path = os.path.join(get_root_directory, 'config', filename + '.yml')
        lock = multiprocessing.Lock()
        lock.acquire()
        file = open(yaml_file_path, 'w')
        yaml.dump(yaml_data, file, default_flow_style=False, sort_keys=False)
        file.close()
        lock.release()
