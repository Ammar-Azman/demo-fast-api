class fakeDB:
    fake_db = {"sara": {"fullname": "Mat Toha", "age": 21, "job": "Hacker"}}

    fake_user_db = {
        "sara": {
            "username": "sara",
            "age": 21,
            "job": "Hacker",
            "disabled": False,
            "hashed_password": "$2y$04$AOvE.7a7e2IJuyEs.ZKWse7/ah42CcymokeFRGfwlpfbAvfb.Dh4q",  # hashed (potato)
        },
        "johndoe": {
            "username": "johndoe",
            "age": 21,
            "job": "Hacker",
            "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
            "disabled": False,
        },
    }
