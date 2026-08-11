from adapters.factory import get_adapter


url = "https://job-boards.greenhouse.io/greenhouse/jobs/8052367?gh_jid=8052367"

adapter = get_adapter(url)

print(type(adapter).__name__)