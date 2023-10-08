import os

n = 3


def generate_music_single(prompt):
    driver = webdriver.Chrome()
    options = webdriver.ChromeOptions()
    download_folder = "/home/starwader/Downloads/"
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    options.add_experimental_option('prefs', {
        "download.default_directory": download_folder,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "plugins.always_open_pdf_externally": True
    })


    driver.get('https://facebook-musicgen.hf.space')
    driver.implicitly_wait(10)
    text_box = driver.find_element(by=By.XPATH, value="/html/body/gradio-app/div/div/div/div/div/div[2]/div[1]/div[1]/div[1]/div/label/textarea")
    submit_button = driver.find_element(by=By.XPATH, value="//*[@id=\"component-12\"]")

    text_box.send_keys(prompt)
    submit_button.click()


    # original button
    download_button_xpath = '/html/body/gradio-app/div/div/div/div/div/div[2]/div[2]/div/div[4]/a/button'

    timeout = 700


    try:
        element_present = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.XPATH, download_button_xpath))
        )
        # Once the element is present, click it
        element_present.click()

        if wait_for_downloads_to_finish(download_folder):
            # Assuming you know the expected filename, or if not, you can grab the latest file
            downloaded_file = max([download_folder  + f for f in os.listdir(download_folder)],
                                  key=os.path.getctime)
            # sound = AudioSegment.from_file(downloaded_file, format="mp4")
            # sound.export("out.wav", format="wav")

            shutil.copy(downloaded_file, os.getcwd())
            print("File copied successfully!")
            return read_file_as_bytes(downloaded_file)

    except Exception as e:
        print(f"Error: {str(e)}")

def generate_music(prompts: list[str]):
    main_prompt = f"""
        Create audio which consists of {n} segments.
        Segments should be distinct.
        Instructions for first segment: {prompts[0]} 
        Instructions for second segment: {prompts[1]} 
        Instructions for third segment: {prompts[2]} 
    """
    for prompt in prompts:
        generate_music_single(prompt) # todo convert mp4
    return bytes()
