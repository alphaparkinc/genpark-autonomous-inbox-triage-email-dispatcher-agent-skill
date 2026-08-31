from client import AutonomousInboxTriageEmailDispatcherAgentClient

def main():
    client = AutonomousInboxTriageEmailDispatcherAgentClient()
    res = client.triage_incoming_email('billing@aws.amazon.com', 'Invoice payment notification for July', 'Your invoice #8812 is available')
    print('Inbox Triage Agent: ' + res['triage_event_id'] + ' (' + res['urgency_priority_level'] + ')')
    print('Sender Tier: ' + res['sender_reputation_tier'] + ' | Action: ' + res['auto_dispatch_action'])
    print('Draft Reply: ' + res['synthesized_draft_reply_text'])
    print('Audit Log: ' + res['audit_trail_log_url'])

if __name__ == '__main__':
    main()
