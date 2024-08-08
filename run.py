"""Running Xetra ETL application"""

import logging
import logging.config
import yaml

def main():
    """
    Entry point to run the Xetra ETL app
    """
    # # Parsin YAML file
    config_path = 'C:\\Users\\Alessandro\\Documents\\Corsi 2024\\Udemy\\Writing production-ready ETL pipelines in Python  Pandas\\xetra_project\\xetra_1234\\configs\\xetra_report1_config.yaml'
    config = yaml.safe_load(open(config_path))
    # configure logging
    log_config = config['logging']
    logging.config.dictConfig(log_config)
    logger = logging.getLogger(__name__)
    logger.info("This is a test.")
    
    
if __name__ == "__main__":
    main()