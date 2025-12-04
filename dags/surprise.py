from airflow.sdk import dag, task

@dag(
    description='Run it and get your gift.',
    schedule=None,
    tags=['surprise', 'gift'],
)
def surprise():
    
    @task
    def look_at_my_logs():
        import os
        import hashlib

        node_selector = os.getenv('ASTRONOMER_NODE_SELECTOR', 'you-must-run-this-dag-on-astro')
        if node_selector == 'you-must-run-this-dag-on-astro':
            print(f"Get your free certification https://academy.astronomer.io/certification-exam-apache-airflow-3-fundamentals?pc={node_selector}")
            return

        hash_object = hashlib.sha256(node_selector.encode())
        hex_hash = hash_object.hexdigest()
        
        positions = [10, 27, 12, 18, 19, 15, 3, 18, 13]
        charset = "0123456789abcdefghijklmnopqrstuvwxyz"
        result = ""
        for pos in positions:
            index = int(hex_hash[pos], 16) % len(charset)
            result += charset[index]

        print(f"Get your free certification https://academy.astronomer.io/certification-exam-apache-airflow-3-fundamentals?pc={result}")

    look_at_my_logs()

surprise()
