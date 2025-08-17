+++
title = 'Firefly III Personal Access Token Expires'
date = 2025-08-16T17:41:40-05:00
draft = false
tags = ['firefly iii','access token']
summary = 'Access tokens expire and do not use the same name.'
comments = true
+++

My personal access token expired.
Not a big deal but when you create a access token,
[Firefly III](https://www.firefly-iii.org/) asks for a name for the token.
After wasting about an hour, I realized that I had two tokens with the same name.
The reason for that I believe is that if you have a token name `firefly_reports`
and delete the old token but you *new* token you call it `firefly_reports`, I
think the software gets confused and either keeps the old one or the new one is
expired using the old date.
Either way, using a different name such as `reports_2025` corrected the issue.

I think this could be a bug but for now I don't think I will issue one since the
fix is to use a different name.

