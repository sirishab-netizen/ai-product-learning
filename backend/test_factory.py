from adapters.factory import get_adapter


url = "https://job-boards.greenhouse.io/greenhouse/jobs/8052367?gh_jid=8052367"

lever_url = "https://jobs.lever.co/gohighlevel/3f9fe900-c62d-4ea6-9712-ad184a3ff7e1"


greenhouse_adapter = get_adapter(url)
lever_adapter = get_adapter(lever_url)


print(type(greenhouse_adapter).__name__)
print(type(lever_adapter).__name__)
