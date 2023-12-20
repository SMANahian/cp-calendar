# How to use
Step 1: Go to <a href="https://cpcalendar.pythonanywhere.com/">This link</a> <br /><br />
Step 2: Select the contest websites you want in your calendar <br /><br />
Step 3: Write the global restricted keywords space separated (Every event with these keywords in name or in contest link will be filtered out so keep it empty if there is no restriction) i.e., "registration youtube" <br /><br />
Step 4: For each website, write the restricted keywords space separated (keep it empty if there is no restriction), i.e., "marathon" in topcoder.com <br /><br />
Step 5: Write the global allowed keywords space separated (Every event of selected websites with these keywords will show up on your calendar. This will override the restriction in Step 4) <br /><br />
Step 6: For each website, write the allowed keywords space separated (If you want every event from this website to show up on calendar except from the restricted ones keep this field empty) i.e., "abc arc agc" in atcoder.jp <br /><br />

Step 7: Copy the link at the end of the form and subscribe to it in your calendar <br /><br />

# Why I made this
For personal use.
I wanted something like <a href="https://clist.by/">Clist Calendar</a> but I needed to filter out some long events from that. So I made this website using <a href="https://clist.by/">Clist API</a> and some filtering options.
