# Mnemosyne.ArcHive – Memory and archive
archive = []

def store_artifact(artifact):
    archive.append(artifact)
    print(f"🧠 Mnemosyne: Artifact stored. Total archived: {len(archive)}")
