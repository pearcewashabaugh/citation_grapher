import configparser


def read_configs():
	config = configparser.ConfigParser()

	config.read('config/config.ini')

	return config