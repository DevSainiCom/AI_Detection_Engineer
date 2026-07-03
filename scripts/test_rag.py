from backend.rag.knowledge_service import knowledge_service


knowledge, sources = knowledge_service.retrieve(
    "Detect Kerberoasting using Event ID 4769"
)

print("=" * 60)

print("Sources")

print(sources)

print("=" * 60)

print(knowledge)