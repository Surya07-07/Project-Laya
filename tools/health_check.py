import compileall

print("=" * 50)
print("PROJECT LAYA HEALTH CHECK")
print("=" * 50)

print()

success = compileall.compile_dir(
    ".",
    quiet=1
)

if success:
    print("✓ All Python files compiled.")
else:
    print("✗ Compilation errors detected.")

print()

print("Health check complete.")
