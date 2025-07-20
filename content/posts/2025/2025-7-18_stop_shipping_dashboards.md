+++
title = "Stop Shipping Dashboards that Don't Matter"
date = 2025-07-20T15:52:37-05:00
draft = false
tags = ['dashboards','career','requirements','Ben Rogojan']
summary = "TLDR, don't forget to do requirements gathering and communicate, communicate, communicate."
comments = true
+++

[Ben's article](https://seattledataguy.substack.com/p/stop-shipping-dashboards-that-dont)
goes through how to not ship dashboards that don't matter.
I think the article also highlights why communication and requirements gathering
is so important.

## Requirements Gathering

I just went through this the past week of so.
I had a request to create a daily production report that could potentially
turn into a dashboard.
He had some good questions to ask:

1. What decision are you trying to make (or action are you trying to make)?
2. What does success look like for you?
3. What do you already know and what assumptions are you working with?

These questions are great not just for a dashboard but good initial questions
for other kinds of projects.
My project for example, they initially wasn't sure if they wanted a daily report
or a dashboard.
Asking similar questions go me closer to getting some requirements.

I developed a mockup after taking what they told me and writing that down as
requirements that I understood.
While I believed that my mockup matched what I was told, I had a meeting with
the stakeholders and got a better idea what they were looking.
They were able to give me a better idea of questions above.
Based on my experience, requirements gathering is a process and is a skill that
will take work and experience.
The less that your stakeholders' skillset matches your own, the more work it
will probably take to get the requirements.

## Communication

Once you have your requirements, your mockup is approved and you deliver your
initial release, make sure to get some feedback.
In the dashboards I create, I log usage.
I don't really care who is using it but if only 5 people are using a dashboard
but 20 people are using a different dashboard, I will focus on the higher usage
all things being equal.
However if those 5 people are upper management and they are using that dashboard
everyday, then that changes my priority.

Unfortunately, reports I typically can't measure usage.
Don't ask, "Is the dashboard/report/etc. useful?" or
"Are you using it and do you any questions?" as these questions makes it too 
easy for the stakeholder to say "Nope, all good.".
Instead, ask questions like
"I noticed that the Ajax production acceptance have been slipping acceptance, are there any other metrics that would be useful?".

Like what Ben mentioned in his article, another way is when you get questions
that implies that they don't use the dashboard or worse ask a dashboard that
you already have done.

## Conclusion

Getting requirements, communication and getting feedback can be the more
difficult, more time than coding.
Don't shortchange yourself doing the requirement phase.
Once you feel comfortable enough with the requirements, any feedback from mockups,
etc., work on your design.
After you have any idea of a design, then provide an estimated completion date.
As you are working on the dashboard/program/etc., any questions, adjustments to
the completion date, make sure and communicate with your stakeholders.
Finally after the release, keep communicating and gathering feedback.
Dashboards can start answering questions but it can also generate more questions.

I highly recommend reading [Ben's article](https://seattledataguy.substack.com/p/stop-shipping-dashboards-that-dont)
as well as potentially signing up to his newsletter.

