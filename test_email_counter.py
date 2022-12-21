import email_count

def test_mbox_long_output(capfd, monkeypatch):
    input = ['mbox-long.txt']
    monkeypatch.setattr('builtins.input', lambda _:input.pop())
    email_count.print_most_emails()
    out, err = capfd.readouterr()
    assert "zqian@umich.edu 195" in out


def test_mbox_short_output(capfd, monkeypatch):
    input = ['mbox-short.txt']
    monkeypatch.setattr('builtins.input', lambda _:input.pop())
    email_count.print_most_emails()
    out, err = capfd.readouterr()
    assert "cwen@iupui.edu 5" in out
    
